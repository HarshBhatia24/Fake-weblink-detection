
# Scam Website Detection App

A machine learning-powered web application that analyzes URLs to detect potentially malicious or scam websites. Built with Flask and scikit-learn, this tool helps users identify dangerous websites before visiting them.

## 🚀 Features

- **Real-time URL Analysis**: Instantly classify websites as "Safe" or "Scam"
- **Machine Learning Model**: Uses logistic regression trained on URL patterns
- **Modern Web Interface**: Clean, responsive design with real-time feedback
- **Comprehensive Error Handling**: Robust validation and error management
- **Pre-trained Dataset**: Includes 200+ safe and scam URL examples

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **Machine Learning**: scikit-learn (Logistic Regression, CountVectorizer)
- **Data Processing**: pandas
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Modern CSS with gradients and animations

## 📁 Project Structure

```
├── main.py              # Flask application and ML model
├── frontend.html        # Web interface
├── safe-urls.csv        # Training data for safe websites
├── scam-urls.csv        # Training data for scam websites
├── pyproject.toml       # Python dependencies
├── .replit              # Replit configuration
└── README.md            # Project documentation
```

## 🚀 Getting Started

### Local Installation

```bash
# Install dependencies
pip install flask pandas scikit-learn

# Run the application
python main.py
```

## 💻 Usage

1. **Open the Web Interface**: Navigate to the application URL
2. **Enter a URL**: Type any website URL in the input field
3. **Analyze**: Click "Analyze Website" or press Enter
4. **View Results**: Get instant feedback on whether the site is safe or potentially dangerous

### Example URLs to Test

**Safe URLs:**
- `https://www.google.com`
- `https://github.com`
- `https://www.wikipedia.org`

**Known Scam Patterns:**
- URLs with suspicious domains
- Fake government portals
- Phishing attempts

## 🤖 Machine Learning Model

### Model Details
- **Algorithm**: Logistic Regression
- **Feature Extraction**: CountVectorizer (bag-of-words)
- **Training Data**: 200+ URLs (safe and scam)
- **Train/Test Split**: 80/20
- **Performance**: Optimized for URL pattern recognition

### How It Works
1. **Data Loading**: Combines safe and scam URL datasets
2. **Feature Extraction**: Converts URLs into numerical features using CountVectorizer
3. **Model Training**: Trains logistic regression on URL patterns
4. **Prediction**: Analyzes new URLs and classifies them as Safe/Scam

## 📊 Dataset

### Safe URLs (`safe-urls.csv`)
- Government websites (.gov.in domains)
- Trusted platforms and services
- Educational institutions
- Legitimate business websites

### Scam URLs (`scam-urls.csv`)
- Phishing attempts
- Fake government portals
- Suspicious domains
- Known malicious URLs

## 🔧 API Endpoints

### GET `/`
Returns the main web interface

### POST `/predict`
Analyzes a URL and returns classification

**Request Body:**
```json
{
  "url": "https://example.com"
}
```

**Response:**
```json
{
  "url": "https://example.com",
  "result": "Safe"
}
```

## 🛡️ Security Features

- **Input Validation**: Validates URL format before processing
- **Error Handling**: Comprehensive exception handling
- **XSS Protection**: Secure frontend implementation
- **Rate Limiting**: Built-in Flask protections

## 🎨 User Interface

- **Responsive Design**: Works on desktop and mobile
- **Modern Styling**: Gradient backgrounds and smooth animations
- **Real-time Feedback**: Loading states and instant results
- **Accessibility**: Clean typography and intuitive layout

## 🔄 Development

### Adding New URLs
1. Add safe URLs to `safe-urls.csv` with label "Safe"
2. Add scam URLs to `scam-urls.csv` with label "Scam"
3. Restart the application to retrain the model

### Improving the Model
- Increase dataset size for better accuracy
- Experiment with different algorithms (Random Forest, SVM)
- Add more sophisticated features (domain age, SSL certificates)

## 📈 Future Enhancements

- [ ] Real-time URL reputation checking
- [ ] Integration with threat intelligence APIs
- [ ] Historical analysis and reporting
- [ ] Batch URL processing
- [ ] User feedback system for model improvement
- [ ] Advanced feature extraction (domain reputation, SSL analysis)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## ⚠️ Disclaimer

This tool is for educational and security awareness purposes. While it aims to detect malicious websites, it should not be the only security measure. Always use updated antivirus software and exercise caution when browsing the internet.

## 📞 Support

For questions or issues, please create an issue in the repository or contact the development team.

---

**Built with ❤️ for a safer internet**
