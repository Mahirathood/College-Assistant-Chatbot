# College Assistant Chatbot - Deployment Guide

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install Flask pandas
```

### 2. Run the Application
```bash
python app.py
```

### 3. Open in Browser
Navigate to: `http://localhost:5000`

## 📁 Project Structure
```
college-assistant-chatbot/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── DEPLOYMENT.md         # This file
├── .gitignore           # Git ignore rules
├── data/
│   └── chat_inputs.csv   # Q&A dataset
├── templates/
│   └── chat.html         # HTML template
├── static/
│   └── chat.css          # CSS styles
└── install_packages.py   # Installation script
```

## 🔧 Features

- **FAQ Matching**: Smart similarity matching using built-in difflib
- **Contextual Responses**: Intelligent fallback for unmatched questions
- **Responsive Design**: Compact widget positioned bottom-left
- **Professional UI**: Clean, modern interface without emojis
- **Lightweight**: Fast installation and startup

## 📝 Customization

### Adding New Q&A Pairs
Edit `data/chat_inputs.csv`:
```csv
question,answer
"Your question here","Your answer here"
```

### Adjusting Similarity Threshold
In `app.py`, modify line 83:
```python
if best_score > 60:  # Change this value (0-100)
```

## 🌐 Deployment Options

### Local Development
```bash
python app.py
```

### Production Deployment
Consider using:
- **Heroku**: Easy cloud deployment
- **Railway**: Simple Python hosting
- **PythonAnywhere**: Free tier available
- **DigitalOcean**: VPS deployment

### Environment Variables
For production, set:
```bash
export FLASK_ENV=production
export FLASK_DEBUG=False
```

## 🐛 Troubleshooting

### Common Issues
1. **Port 5000 busy**: Change port in `app.py`
2. **CSV not found**: Ensure `data/chat_inputs.csv` exists
3. **Import errors**: Run `pip install -r requirements.txt`

### Performance Tips
- Use gunicorn for production: `pip install gunicorn`
- Enable caching for static files
- Consider using a database for large datasets

## 📞 Support
For issues or questions, please create an issue in the GitHub repository.
