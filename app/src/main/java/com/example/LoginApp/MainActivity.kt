package com.example.LoginApp

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Toast

class MainActivity : AppCompatActivity() {

    lateinit var editUser: EditText
    lateinit var editPassword: EditText
    lateinit var doLogin: Button
    lateinit var doRegistration: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
       setContentView(R.layout.activity_main)

        doRegistration = findViewById(R.id.signup)
        editUser = findViewById(R.id.username)
        editPassword = findViewById(R.id.password)
        doLogin = findViewById(R.id.loginButton)

        doRegistration.setOnClickListener{
            startActivity(Intent(this,Registration::class.java))
        }

        doLogin.setOnClickListener{
            if(editUser.text.toString() == "user" && editPassword.text.toString() == "1234"){
                Toast.makeText(this,"login Successful!",Toast.LENGTH_SHORT).show()
                startActivity(Intent(this,HomeActivity::class.java))
            }else{
                Toast.makeText( this, "Login Failed!", Toast.LENGTH_SHORT).show()
            }
        }

    }
}