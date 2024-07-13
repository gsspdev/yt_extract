# yt_extact

A command-line tool to extract fields from  output of other command-line tools.

## Setup

1. Ensure you have Python 3.6 or later installed.

2. Clone this repository:
   ```
   git clone https://github.com/yourusername/yt_extract.git
   cd yt_extract
   ```

3. Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the tool:
   ```
   pip install .
   ```

## Usage

After installation, you can use the tool as follows:

```
yt-extract "your_command_here" field1 field2.nested_field field3 --output yt
```

For example:

```
yt-extract "curl -s https://api.example.com/user/123" name email address.city --output yt
```

This will run the specified command, parse its yt output, and extract the requested fields.

## Options

- `command`: The command to run (required)
- `fields`: One or more fields to extract from the yt output (required)
- `--output`: Output format, either "yt" or "text" (optional, defaults to "text")

## License

This project is licensed under the MIT License.
