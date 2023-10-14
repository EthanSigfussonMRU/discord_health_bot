import gpt_integration

# further expanded for different cases such as requesting sleep schedual
# excersice commenting
# eating habbits
# mental wellness check
def get_response(message: str) -> str:
    return gpt_integration.accost_gpt(f"'''{message}'''")