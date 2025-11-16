from flask import Flask, render_template, request, redirect, url_for
import model

app = Flask(__name__)

# Data structure and constant naming
VALID_USER_IDS = {
    'joshua', 'dorothy w', 'rebecca', 'samantha', 'raeanne', 'kimmie', 
    'cassie', 'nicole', 'jkell', 'karen', 'warren', 'amanda', 
    'birdwoman', 'michelle', 'zippy'
}
VALID_USER_IDS_LIST = list(VALID_USER_IDS)

@app.route('/')
def home_view():
    """Renders the main page."""
    return render_template('index.html', valid_users=VALID_USER_IDS_LIST)

@app.route('/recommend', methods=['POST'])
def recommend_top5():
    """Handles user input, validates, and returns recommendations or an error message."""
    
    #Clean variable naming and immediate retrieval
    user_name = request.form.get('User Name', '').strip()
    
    #Logging: Use f-strings and be specific about what's logged.
    print(f"Received recommendation request for user: '{user_name}'")
    
    # Check if the username is valid
    if user_name in VALID_USER_IDS:
        try:
            top20_products = model.recommend_products(user_name)
            get_top5 = model.top5_products(top20_products)
            
            # Prepare data for rendering
            template_data = {
                'column_names': get_top5.columns.values,
                'row_data': list(get_top5.values.tolist()),
                'text': 'Top 5 recommended products for user:',
                'user': user_name,
                'valid_users': VALID_USER_IDS_LIST,
                # 'zip' is available by default in Jinja, no need to pass it explicitly
            }
            return render_template('index.html', **template_data)
        
        except Exception as e:
            #Error Handling: If model fails, log and show a graceful error.
            print(f"Error during recommendation for user {user_name}: {e}")
            return render_template('index.html', 
                                   text=f'An error occurred while fetching recommendations for user:',
                                   user=user_name,
                                   valid_users=VALID_USER_IDS_LIST)

    # If the user is invalid OR the user_name is empty (empty string is not in the set)
    else: 
        # Only show a message if a user was actually typed/submitted
        if user_name:
             return render_template('index.html',
                                   text=f'User not found in the review knowledge base:',
                                   user=user_name,
                                   valid_users=VALID_USER_IDS_LIST 
                                   )
        # If the request was POSTed but the field was empty, redirect home
        return redirect(url_for('home_view'))

# --- Application Startup ---
if __name__ == '__main__':
    app.run(debug=False)