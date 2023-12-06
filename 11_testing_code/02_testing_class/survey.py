class AnonymusSurvey:
    """Collect anonymus answers to a survey question."""

    def __init__(self, question) -> None:
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses: list[str] = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses to the survey."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
