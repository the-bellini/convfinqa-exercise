import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Customize the format
    datefmt="%Y-%m-%d %H:%M:%S",  # Set the date format
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file
        logging.StreamHandler(),  # Log to console
    ],
)

# Create a logger
logger = logging.getLogger(__name__)


def execute_calculation(calculation_str: str | None) -> float | None:
    """
    Evaluates a given calculation string as a Python expression and returns the result.

    Args:
        calculation_str (str): The calculation in string format to be evaluated.

    Returns:
        float: The result of the evaluated calculation.
        None: If the calculation cannot be evaluated.

    Raises:
        ValueError: If the calculation is not a numeric value.
    """
    if calculation_str:
        try:
            # Evaluate the string as a Python expression
            result = eval(calculation_str)
            if not isinstance(result, (int, float)):
                raise ValueError("The result is not a numeric value.")
            return float(result)
        except Exception as e:
            logger.debug(f"Error evaluating calculation: {e}")
            return None
    return None
