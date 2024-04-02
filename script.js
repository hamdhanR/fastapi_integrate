document.getElementById("login-form").addEventListener("submit", async function(event) {
    event.preventDefault(); // Prevent form submission
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    
    // Here you can add your validation logic
    if (username !== "" && password !== "") {
        try {
            let response = await fetch("http://localhost:8000/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({name: username, password: password})
            });
            if (response.ok) {
                // Handle successful login\
                let a=await response.json();
                console.log(a);
            } else {
                // Handle other response statuses (e.g., server errors)
                console.error("Login failed");
            }
        } catch (error) {
            // Handle network errors
            console.error("Network error:", error);
        }
    } else {
        document.getElementById("error-message").textContent = "Invalid username or password";
    }
});
