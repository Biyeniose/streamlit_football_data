import os
from pathlib import Path
from supabase import create_client, Client
from dotenv import load_dotenv
#dotenv_path = Path('../')
# Load environment variables from .env file
load_dotenv()

# Get Supabase credentials from environment variables
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

# Create the Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Export the Supabase client
#__all__ = ['supabase']
