from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class Resource:
    def __init__(self, cpu, memory, storage):
        self.cpu = cpu
        self.memory = memory
        self.storage = storage

    def allocate(self, cpu_demand, memory_demand, storage_demand):
        if (self.cpu >= cpu_demand) and (self.memory >= memory_demand) and (self.storage >= storage_demand):
            self.cpu -= cpu_demand
            self.memory -= memory_demand
            self.storage -= storage_demand
            return True
        else:
            return False

# Create on-premise resource object
on_premise_resources = Resource(cpu=8, memory=32, storage=1000)

class MyRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Serve the HTML page directly
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        response_html = self.get_html_response("")
        self.wfile.write(response_html.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        post_params = urllib.parse.parse_qs(post_data)

        # Extract resource demands
        cpu_demand = int(post_params.get('cpu', [0])[0])
        memory_demand = int(post_params.get('memory', [0])[0])
        storage_demand = int(post_params.get('storage', [0])[0])

        # Allocate resources
        if on_premise_resources.allocate(cpu_demand, memory_demand, storage_demand):
            response_message = f"Resources allocated from on-premises: {cpu_demand} CPUs, {memory_demand} GB Memory, {storage_demand} GB Storage."
        else:
            response_message = f"Insufficient on-premises resources. Resources allocated from cloud: {cpu_demand} CPUs, {memory_demand} GB Memory, {storage_demand} GB Storage."

        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        response_html = self.get_html_response(response_message)
        self.wfile.write(response_html.encode('utf-8'))

    def get_html_response(self, response_message):
        return f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Hybrid Cloud Resource Allocation</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin: 0;
                    padding: 0;
                    background: url('https://logicalfront.com/wp-content/uploads/2023/08/CLoud-resource-Allocation_0-thegem-blog-timeline-large.jpg') no-repeat center center fixed;
                    background-size: cover;
                    color: white;
                }}
                h1 {{
                    margin-top: 50px;
                    color: white;
                    text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.7);
                }}
                input, button {{
                    padding: 10px;
                    margin: 10px;
                    font-size: 1rem;
                    border: 1px solid #007BFF;
                    border-radius: 5px;
                }}
                button {{
                    background-color: #007BFF;
                    color: white;
                    border: none;
                    cursor: pointer;
                    transition: background-color 0.3s ease;
                }}
                button:hover {{
                    background-color: #0056b3;
                }}
                .result {{
                    background-color: rgba(255, 255, 255, 0.8);
                    border-radius: 10px;
                    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
                    padding: 20px;
                    margin: 20px auto;
                    max-width: 600px;
                    color: #333;
                    transition: transform 0.2s;
                }}
                .result:hover {{
                    transform: scale(1.02);
                }}
                .result h2 {{
                    color: #28a745;
                }}
            </style>
        </head>
        <body>
            <h1>Hybrid Cloud Resource Allocation</h1>
            <form action="/" method="POST">
                <label for="cpu">CPU Demand (cores):</label>
                <input type="number" id="cpu" name="cpu" required><br>
                <label for="memory">Memory Demand (GB):</label>
                <input type="number" id="memory" name="memory" required><br>
                <label for="storage">Storage Demand (GB):</label>
                <input type="number" id="storage" name="storage" required><br>
                <button type="submit">Allocate Resources</button>
            </form>

            <div class="result">
                <h2>Result</h2>
                <p>{response_message}</p>
            </div>
        </body>
        </html>
        '''

# Define server address and port
server_address = ('0.0.0.0', 5000)
httpd = HTTPServer(server_address, MyRequestHandler)

print("Server running on port 5000...")
httpd.serve_forever()
