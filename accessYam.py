import yaml

# Example YAML content (can also be loaded from a file)

yaml_content = """
person:
  name: John Doe
  age: 30
  hobbies:
    - reading
    - cycling
"""

# Parse the YAML content
data = yaml.safe_load(yaml_content)

# Access specific items
print(data['person']['name'])
print(data['person']['hobbies'][0])