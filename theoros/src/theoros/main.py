#!/usr/bin/env python
import os
import warnings

from theoros.crew import Theoros

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    query = os.getenv(
        "QUERY_STRING", 
        "Who were the screenwriters Avengers: Endgame")
    inputs = {
        'query': query,
    }

    try:
        Theoros().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()