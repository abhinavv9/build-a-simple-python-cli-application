# Build a Simple Python CLI Application

This project is a basic command-line interface (CLI) application built in Python using the `argparse` module. It demonstrates how to create an executable script that accepts command-line arguments.

## Features

*   Parses an optional `--name` argument.
*   Parses an optional `--greeting` argument.
*   Defaults to greeting 'World' with 'Hello' if no arguments are provided.

## Prerequisites

*   Python 3 installed on your system.

## Setup

1.  Clone the repository:
    ```bash
    git clone <repository-url>
    cd build-a-simple-python-cli-application
    ```

2.  Ensure you have Python 3 installed.

## Usage

To run the application, navigate to the `src` directory in your terminal and execute the `main.py` script.

**Default greeting:**

```bash
python src/main.py
```

Output:

```
Hello, World!
```

**With a custom name:**

```bash
python src/main.py --name Alice
```

Output:

```
Hello, Alice!
```

**With a custom greeting and name:**

```bash
python src/main.py --greeting "Good morning" --name Bob
```

Output:

```
Good morning, Bob!
```

**Making the script executable (on Unix-like systems):**

```bash
chmod +x src/main.py
./src/main.py --name Charlie
```

Output:

```
Hello, Charlie!
```

## Project Structure

```
build-a-simple-python-cli-application/
├── src/
│   └── main.py
└── README.md
```

## Contributing

This is a simple example project. Contributions are welcome if you have suggestions for improvements or new features.
