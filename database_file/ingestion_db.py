{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "28ef71a3-ebf7-4429-aeae-85a884e3f418",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sqlalchemy import create_engine\n",
    "import os\n",
    "import logging\n",
    "import time\n",
    "\n",
    "logging.basicConfig(\n",
    "    filename=\"logs/ingestion_db.log\",\n",
    "    level=logging.DEBUG,\n",
    "    format=\"%(asctime)s - %(levelname)s - %(message)s\",\n",
    "    filemode=\"a\"\n",
    ")\n",
    "\n",
    "engine=create_engine('sqlite:///inventory.db')\n",
    "\n",
    "\n",
    "def ingest_db(df,table_name,engine):\n",
    "  ''' this function will ingest the dataframe into database table'''\n",
    "  df.to_sql(table_name,con=engine,if_exists='replace',index=False)\n",
    "\n",
    "def load_raw_data():\n",
    "  ''' this function will load the CSVs as dataframe and ingest into db'''\n",
    "  start= time.time()\n",
    "  for file in os.listdir('data'):\n",
    "    if file.endswith('.csv'):\n",
    "        table_name=file[:-4]\n",
    "        logging.info(f'Ingesting {file} in table:{table_name}')\n",
    "        df=pd.read_csv(os.path.join('data' , file),chunksize=5000)\n",
    "        first_chunk=True\n",
    "        for dataframe in df:\n",
    "            if_exists_mode = 'replace' if first_chunk else 'append'\n",
    "            dataframe.to_sql(table_name,con=engine,if_exists=if_exists_mode,index=False)\n",
    "            first_chunk=False\n",
    "        \n",
    "    end=time.time()\n",
    "    total_time=(end-start)/60\n",
    "  logging.info(\" ---------------Data Ingestion completed---------------\")\n",
    "  logging.info(f\"Total time taken: {total_time:.2f} minutes\")\n",
    "\n",
    "if __name__=='__main__':\n",
    "  load_raw_data()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6b9d8307-dd75-451e-ac9b-5a8ad69ecb94",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c1a4b459-6d73-4c68-b5c4-9a4d886f85a4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
