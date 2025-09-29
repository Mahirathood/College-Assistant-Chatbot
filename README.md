# College Assistant Chatbot

A lightweight, web-based chatbot for college student query assistance built with Python Flask and intelligent FAQ matching.

##  Features

-  **Smart FAQ Matching**: Intelligent similarity matching using built-in Python libraries
-  **College Knowledge Base**: Pre-loaded with common college queries and responses
-  **Contextual Responses**: Intelligent fallback responses for unmatched questions
-  **Responsive Design**: Compact widget positioned bottom-left with professional styling
-  **Lightweight**: Fast installation and startup with minimal dependencies
-  **Easy Customization**: Simple CSV-based knowledge management

## Project Structure

```
bot/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── data/
│   └── chat_inputs.csv   # Q&A dataset
├── templates/
│   └── chat.html         # HTML template
└── static/
    └── chat.css          # CSS styles
```

## Installation & Setup

### Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

### Step 3: Open in Browser

Open your web browser and navigate to `http://localhost:5000`

##  How It Works

### 1. FAQ Matching (Primary)
- Uses Python's built-in `difflib` for similarity comparison
- Threshold of 60% similarity required for a match
- Returns pre-defined answers from your CSV dataset

### 2. Intelligent Fallback (Secondary)
- Context-aware responses for unmatched questions
- Keyword recognition for greetings, thanks, help requests
- Professional fallback messages for unknown queries

### 3. Smart Features
- Input validation and error handling
- Responsive design for all devices
- Clean, professional interface

## Configuration

### Adjusting FAQ Matching Threshold
In `app.py`, modify the threshold value:
```python
if best_score > 60:  # Change this value (0-100)
    return best_answer
```

### Adding New Q&A Pairs
Edit `data/chat_inputs.csv` and add new rows:
```csv
question,answer
"Your question here","Your answer here"
```

##  Troubleshooting

### Common Issues

1. **Port Already in Use**
   - Change port in `app.py`:
   ```python
   app.run(debug=True, host='0.0.0.0', port=5001)  # Change 5000 to 5001
   ```

2. **CSV File Not Found**
   - Ensure `data/chat_inputs.csv` exists
   - Check file path in `app.py`

3. **Import Errors**
   - Install dependencies: `pip install -r requirements.txt`
   - Use Python 3.7 or higher

### Performance Tips
- The app starts instantly (no model loading)
- Uses minimal memory (~50MB)
- Perfect for lightweight deployment

## Development

### Adding New Features

1. **New Response Types**: Modify `get_response()` function
2. **UI Changes**: Edit `templates/chat.html` and `static/chat.css`
3. **Data Management**: Update CSV structure and loading logic

### Testing

Test the chatbot with various inputs:
- Exact matches from dataset
- Similar but not exact questions
- Completely new questions
- Edge cases (empty input, special characters)

## 🛠️ Technologies Used

- **Backend**: Flask (Python web framework)
- **Similarity Matching**: Python's built-in difflib
- **Frontend**: HTML5, CSS3, jQuery
- **Data**: Pandas for CSV handling
- **Styling**: Custom CSS with responsive design

## License

This project is open source and available under the MIT License.

##  Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Acknowledgments

- Built with Flask and Python
- Inspired by modern chatbot interfaces
- Designed for educational institutions

##  Support

For issues or questions:
1. Check the [troubleshooting](#-troubleshooting) section
2. Create an issue in this repository
3. Contact: [your-email@example.com]

---

 **Star this repository if you find it helpful!**
