package com.example.loginandsignup

import android.annotation.SuppressLint
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Toast

class MainActivity : AppCompatActivity() {

    lateinit var doLogin: Button
    lateinit var doregistration: Button

    lateinit var editUName: EditText
    lateinit var editUPassword: EditText

    @SuppressLint("MissingInflatedId")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        doLogin = findViewById(R.id.loginButton)
        doregistration = findViewById(R.id.signupButton)
        editUName = findViewById(R.id.editUsername)
        editUPassword = findViewById(R.id.editPassword)
        doLogin.setOnClickListener {

            if(editUName.text.toString() == "user" && editUPassword.text.toString() == "12345"){
                Toast.makeText(this,"login Successful!", Toast.LENGTH_SHORT).show()
                startActivity(Intent(this, HomeActivity::class.java)
                    .putExtra("username",editUName.text.toString()))
            }else{
                Toast.makeText( this, "Login Failed!", Toast.LENGTH_SHORT).show()
            }

        }

        doregistration.setOnClickListener{
            startActivity(Intent(this,RegistrationActivity::class.java))
        }


    }
}