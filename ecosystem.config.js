module.exports = {
  apps: [
    {
      name: 'streamlit',
      script: 'streamlit',
      interpreter: 'none',
      args: 'run --server.enableCORS false app_streamlit.py',
      env: {
        "PYTHONUNBUFFERED": "1",
        "PORT": "8501"
      }
    }
  ]
};
