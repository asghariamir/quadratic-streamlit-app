
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Quadratic Equation Explorer")

# Sliders for coefficients
a = st.slider("Choose a", -10.0, 10.0, 1.0)
b = st.slider("Choose b", -10.0, 10.0, 0.0)
c = st.slider("Choose c", -10.0, 10.0, 0.0)

# Display the equation
st.latex(f"{a}x^2 + {b}x + {c} = 0")

# Calculate discriminant and roots
D = b**2 - 4*a*c

if a == 0:
    st.warning("This is not a quadratic equation.")
else:
    if D > 0:
        root1 = (-b + np.sqrt(D)) / (2*a)
        root2 = (-b - np.sqrt(D)) / (2*a)
        st.success(f"Two real roots: x = {root1:.2f}, x = {root2:.2f}")
    elif D == 0:
        root = -b / (2*a)
        st.success(f"One real root: x = {root:.2f}")
    else:
        real = -b / (2*a)
        imag = np.sqrt(-D) / (2*a)
        st.info(f"Complex roots: x = {real:.2f} ± {imag:.2f}i")

    # Optional: plot the function
    st.subheader("Graph of the equation")
    x = np.linspace(-10, 10, 400)
    y = a*x**2 + b*x + c
    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"{a}x² + {b}x + {c}")
    ax.axhline(0, color='gray', linestyle='--')
    ax.axvline(0, color='gray', linestyle='--')
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    st.pyplot(fig)
