import sys, os
import pandas as pd
import pantab as pt


def prinf(*vrs):
  print(*vrs)
  

def csv_to_df(input_file):
  """ Read data from CSV files"""
  
  if not input_file.endswith(".csv"):
    print(f"Invalid file: {input_file}")
    sys.exit()
    
  if not os.path.exists(input_file):
    print(f"Invalid path: {input_file}")
    sys.exit()
    
  #print(f"Reading data from: {input_file}")
    
  df = pd.read_csv(input_file)
  
  return df


def csv_to_hyper(input_files, dest_file = "sample.hyper", sch_name = "Extract", tbl_name = "Extract"):
  """
  Import file contents into Hyperfile Schema/Table
  args:
  
  return boolean
  """
  if not isinstance(input_files, list):
    input_files = [input_files]
    
  if not dest_file.endswith(".hyper"):
    print(f"Invalid destination file: {dest_file}")
    sys.exit()
    
  for input_file in input_files:
    print(f"Importing file: {input_file}")
    
    df_in = pd.read_csv(input_file)
    
    #df_in.head()
    
    try:
      print(f"Loading data into hyperfile: {dest_hyper}")
      #pt.frame_to_hyper(df=df_in, database=dest_hyper, table=tbl_name, table_mode="a")
      pt.frame_to_hyper(df=df_in, database=dest_hyper, table=tbl_name)
      print("Done loading data!")
    except:
      print(f"ERROR - unable to load data into {dest_hyper}")
    
    
    
  
  
