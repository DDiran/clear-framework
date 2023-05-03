# CLEAR Framework Prompt Analyser

🔗 [Live Demo](https://hackathonclear.pythonanywhere.com)

The CLEAR Prompt Analyser is a Flask-based web application that leverages OpenAI's ChatGPT API to analyze and evaluate prompts using the C.L.E.A.R. Prompts framework.

## Table of Contents

- [CLEAR Framework Prompt Analyser](#clear-framework-prompt-analyser)
  - [Table of Contents](#table-of-contents)
  - [Background](#background)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Acknowledgements](#acknowledgements)

## Background

This project was created during Hackathon 21. Both the CLEAR Framework and this app were entirely created by ChatGPT (using v4 of the model). The analysis is performed by ChatGPT as well, using v3.5.

I've also included an option to download and use an open-source model (GPT-2) for free but it wasn't clever enough to use the framework to analyse prompts, and I ran out of time to find one which could work. You can find the working code in the **dev** branch.

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or higher
- Flask
- OpenAI

### Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/DDiran/clear-framework.git
cd clear-app
```

1. Create and activate a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

1. Install the required Python packages:

```
pip install -r requirements.txt
```

1. Set up your OpenAI API key:

```
export OPENAI_API_KEY=your_api_key_here
```

## Usage

To run the application, use the following command:

```
flask run
```

Open your web browser and visit `http://127.0.0.1:5000/` to access the application.

## Acknowledgements

- ChatGPT for building everything (including this README.md file)
- BulmaCSS for very quick and dirty styling
- Alpine.js for lightweight interactivity
