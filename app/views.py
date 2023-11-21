from django.shortcuts import render
import subprocess
from scripts.runbutton import MyBot  # Adjust the import based on your project structure

def runbutton(request):
    if request.method == 'POST':
        # Get the URL input from the form
        url_input = request.POST.get('urlInput', '')

        try:
            # Run your Python script using subprocess
            result = subprocess.run(['python', 'scripts/runbutton.py', url_input],
                                    capture_output=True, text=True, check=True)

            # Check if the subprocess ran successfully
            if result.returncode == 0:
                output = result.stdout
                # Create an instance of the MyBot class with the user-inputted URL
                MyBot(url_input)

                # Add code to capture the screenshot and pass it to the template
                screenshot_path = 'screenshot.png'
                return render(request, 'app/runbutton.html', {'output': output, 'screenshot_path': screenshot_path})

            else:
                # If the subprocess failed, log the error and return an error response
                error_message = result.stderr if result.stderr else "Script execution failed"
                # Log the error for debugging purposes
                print(f"Error executing script: {error_message}")
                return render(request, 'app/runbutton.html', {'error': error_message})

        except subprocess.CalledProcessError as e:
            # Log the subprocess error for debugging purposes
            print(f"Subprocess error: {str(e)}")
            return render(request, 'app/runbutton.html', {'error': f"Subprocess error: {str(e)}"})

        except Exception as e:
            # Log the general exception for debugging purposes
            print(f"Unexpected error: {str(e)}")
            return render(request, 'app/runbutton.html', {'error': f"Error executing script: {str(e)}"})

    # If not a POST request, render the initial form
    return render(request, 'app/runbutton.html')
