import json

def display_endpoints(swagger_data):
    paths = swagger_data.get('paths')
    if paths:
        for path, methods in paths.items():
            print(f"Path: {path}")
            for method, details in methods.items():
                print(f"  Method: {method}")
            print()

if __name__ == '__main__':
    # Assuming the Swagger file is named 'swagger.json' in the same directory
    with open('swagger.json', 'r') as file:
        try:
            swagger_data = json.load(file)
            display_endpoints(swagger_data)
        except json.JSONDecodeError as e:
            print(f"Error loading JSON: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

