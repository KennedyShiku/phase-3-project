# Social Media Marketing Agency (SMMA) Management System

## Overview

This project is a Social Media Marketing Agency (SMMA) Management System implemented in Python using SQLAlchemy and Click for command-line interaction.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.9 or higher
- Pipenv

### Installation

1. Clone the repository:

   ```bash```

   git clone [https://github.com/KennedyShiku/phase-3-project](https://github.com/your-username/smma-management-system.git)


    Change to the project directory:
    ```bash```

        cd smma-management-system


### Create a virtual environment:
```bash```

    pipenv install


This will install the required dependencies.

## Usage
### Initializing the Database

To initialize the database with initial marketers, run:
```bash```

      pipenv run python cli.py initialize_database

### Adding a Client

To add a new client, run:

```bash```

    pipenv run python cli.py add_client


Follow the prompts to enter the client name, type of content to be marketed, and choose a marketer.

### Removing a Client

To remove a client and associated content, run:

```bash```

    pipenv run python cli.py remove_client


Follow the prompt to enter the ID of the client to remove.

### Querying and Printing a Client

To query and print a client, run:

```bash```

    pipenv run python cli.py query_and_print_client

### Displaying Tables

To display contents of clients, contents, and marketers tables, run:

```bash```

    pipenv run python cli.py display_tables


## Contributing

Contributions are welcome! If you find any issues or have improvements to suggest, please open an issue or submit a pull request.

## License

### MIT License

Copyright © 2023 Kennedy Rich

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

