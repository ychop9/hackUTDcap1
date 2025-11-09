FinReflect: Meet Your Future Self

FinReflect is a single-page HTML application that serves as a financial mirror. 
It allows users to log manual income and expense transactions in real-time using Google Firestore for persistent storage and displays a dynamic dashboard using Chart.js to visualize spending habits.
This project requires Firebase for persistence and must be run via a local web server (not file://).

1. Firebase Setup

You need a Firebase Project with Firestore and Authentication enabled.

A. Console Configuration

Create a Project in the Firebase Console and register a new Web App.

Enable Firestore Database (start in production mode).

Enable the Anonymous sign-in method under Authentication.

Ensure your Firestore Security Rules permit read/write access for authenticated users to the path: artifacts/{appId}/users/{userId}/transactions.

B. index.html Configuration

Locate the global variables in the <script type="module"> block of index.html and replace the placeholder values with your actual Firebase Web App credentials:

const firebaseConfig = {
    apiKey: "AIzaSy_YOUR_API_KEY", // <-- REQUIRED
    authDomain: "your-project-id.firebaseapp.com",
    projectId: "your-project-id", // <-- REQUIRED
    // ... rest of config
};


2. Running Locally

The app must be served by a local HTTP server to properly load JavaScript modules and handle network requests.

Use Python (Recommended):

Navigate to the directory containing index.html.

Run: python3 -m http.server 8080

Open: http://localhost:8080

3. Development Issues
We had a lot of trouble debugging and creating this project as we are still novice programmers in html and javascript. We also were not fully familiar with the Firebase implementation which took a lot
of time and effort to understand. We had to utilize a lot of youtibe tutorials and other resources to finish our project. Due to the time and knowledge constraints we weren't able to
fully elaborate all the features of our web app. We plan to fully develop this in the future so we can make this into a full scalable web app that people can use in real time.
