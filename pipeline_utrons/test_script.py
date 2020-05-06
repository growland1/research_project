import os 

current_file = __file__
pipeline_path = os.path.abspath(current_file)
pipeline_directory = os.path.dirname(pipeline_path)
script_path = "pipeline_utrons/find_utrons.py"
full_utron_path = os.path.join(pipeline_directory, script_path)
print (full_utron_path)

