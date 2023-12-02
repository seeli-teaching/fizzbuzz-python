import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# Passing data to the function via route parameter
# Example: http://localhost:7071/api/parameter_by_route/Markus


@app.route(route="FizzBuzz/{number}")
def parameter_by_route(req: func.HttpRequest) -> func.HttpResponse:

    # Get the value of the route parameter
    number_as_string = req.route_params.get('number')
    logging.info(f"FizzBuzz called with {number_as_string}")

    # Convert the string to a number

    # do your magic here

    result = ""

    logging.info(result)

    # a http triggered function always returns a http-response
    return func.HttpResponse(result)
