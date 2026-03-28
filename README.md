CampusPulse: Giving University Resources a Brain
Honestly, there’s nothing more frustrating than hauling your laptop all the way to the library just to find out every single desk is taken. That’s exactly why I started CampusPulse. It’s a project designed to take the guesswork out of campus life by using a bit of Machine Learning and NLP to predict crowd levels before you even leave your dorm.

What’s the Goal?

The idea is pretty straightforward:
•	Stop the Guessing: We use historical data to forecast exactly how busy the library or canteen will be at any given hour.
•	Actually Listen to Students: Instead of letting feedback rot in a database, our system automatically categorizes student reviews so administrators can see what’s actually broken.
•	Theory in the Wild: This was a chance to take classroom concepts—like Linear Regression and Transfer Learning—and see if they actually hold up in a real-world scenario.

The Tech Stack

I went with a modular Python setup to keep things from getting messy. If you're looking under the hood, here’s what’s running:
•	The Basics: Python 3.13.
•	The Heavy Lifters: Pandas and NumPy for all the data manipulation.
•	The Intelligence: We’re using Scikit-learn for the predictive side and TextBlob to figure out the "vibe" (sentiment) of student feedback.

Want to Run It?

If you've got Python installed, getting this up and running is a three-step process:
1.	Clone the Repo: git clone [https://github.com/yourusername/campus-pulse-ai.git]
2.	Install the Goods: Pop open your terminal and run pip install pandas scikit-learn textblob.
3.	Launch: Execute python main.py and you'll see the model start its thing.

The Methodology (The "Science" Bit)

Predicting the Crowds (CO4): We’re using a Linear Regression model here. It looks at the "Hour" and whether it’s "Exam Week" to spit out an occupancy percentage. To make sure we aren't totally off base, we use Mean Squared Error (MSE) to keep an eye on the bias-variance tradeoff.
Decoding the Feedback (CO5): For the sentiment analysis, we’re leaning on Transfer Learning. By using a pre-trained NLP model, the system can instantly tell if a student's review is positive, negative, or just "meh" (neutral). It’s basically an automated pulse-check for the campus.
________________________________________
A Quick Note: This was built as a "Bring Your Own Project" (BYOP) for the VITyarthi AI Course. It's open-source, so feel free to use it for your own research or just to see how the models work.
Appendex:
<img width="2179" height="1268" alt="Screenshot 2026-03-28 101047" src="https://github.com/user-attachments/assets/a1b0f94e-bcf6-4a51-ba8f-25240ee27fb9" />
<img width="2183" height="1420" alt="Screenshot 2026-03-28 101111" src="https://github.com/user-attachments/assets/5963ee40-ecb8-4e4d-b08d-0ce24a026e7b" />
<img width="2165" height="1799" alt="Screenshot 2026-03-28 101034" src="https://github.com/user-attachments/assets/11dcdbd5-421a-49f1-b8df-83423b3ac760" />
