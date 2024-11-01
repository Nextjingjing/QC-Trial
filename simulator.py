import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
import random
from math import comb

# Define the theoretical Pa calculation function
def calculate_pa(n, p, c):
    """Calculate Probability of Acceptance (Pa) for binomial sampling."""
    pa = sum(comb(n, k) * (p ** k) * ((1 - p) ** (n - k)) for k in range(0, c + 1))
    return pa

# Define the simulation function for Pa using random sampling
def simulate_pa(n, p, c, trials):
    """Simulate Probability of Acceptance (Pa) using random sampling."""
    successes = 0
    for _ in range(trials):
        count = sum(1 for _ in range(n) if random.random() < p)
        if count <= c:
            successes += 1
    return successes / trials

# Define parameters
n_values = range(5, 100)   # Sample sizes from 5 to 20
trial_values = [10, 500]  # Different numbers of trials for simulation

# Initial values for p and c
p = 0.1
c = 10

# Function to update the plot with new p and c values
def update_plot(p, c):
    p = float(p)
    c = int(c)
    
    # Calculate theoretical Pa values for comparison
    theoretical_pa_values = [calculate_pa(n, p, c) for n in n_values]
    simulated_pa_values_10 = [simulate_pa(n, p, c, trials=10) for n in n_values]
    simulated_pa_values_500 = [simulate_pa(n, p, c, trials=500) for n in n_values]

    # Clear and update plot
    ax.clear()
    ax.plot(n_values, theoretical_pa_values, label='Theoretical Pa', linestyle='-')
    ax.plot(n_values, simulated_pa_values_10, label='Simulated Pa (10 trials)', linestyle=':')
    ax.plot(n_values, simulated_pa_values_500, label='Simulated Pa (500 trials)', linestyle='--')
    ax.set_xlabel('Sample Size (n)')
    ax.set_ylabel('Probability of Acceptance (Pa)')
    ax.set_title('Comparison of Theoretical and Simulated Pa Values with Different Trial Counts')
    ax.legend()
    ax.grid(True)
    # Annotate p and c values in the bottom-left corner
    ax.text(min(n_values), min(theoretical_pa_values) * 1.05, f'p = {p}, c = {c}', fontsize=12, color='red',
            verticalalignment='bottom', horizontalalignment='left')
    plt.draw()

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.3)

# Initial plot with default values
update_plot(p, c)

# Adjusted positions for text boxes
axbox_p = plt.axes([0.30, 0.15, 0.15, 0.05])  # Position for p input box with more space on left
axbox_c = plt.axes([0.55, 0.15, 0.15, 0.05])  # Position for c input box with more separation

text_box_p = TextBox(axbox_p, 'Probability of Defect:', initial=str(p))
text_box_c = TextBox(axbox_c, 'Acceptance:', initial=str(c))

# Define the function to be called when text is submitted
def submit(text):
    try:
        new_p = text_box_p.text
        new_c = text_box_c.text
        update_plot(new_p, new_c)
    except ValueError:
        pass

# Connect the submit function to both text boxes
text_box_p.on_submit(submit)
text_box_c.on_submit(submit)

plt.show()
