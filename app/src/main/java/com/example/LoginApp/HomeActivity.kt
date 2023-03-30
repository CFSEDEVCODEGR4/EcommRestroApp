package com.example.LoginApp

import android.annotation.SuppressLint
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView

class HomeActivity : AppCompatActivity() {
    lateinit var textUser :TextView
    lateinit var textEmail:TextView

    @SuppressLint("MissingInflatedId")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_home)

        textUser = findViewById(R.id.show_username)
        textEmail = findViewById(R.id.show_email)

        val username = intent.getStringExtra("username")
        val email = intent.getStringExtra("email")

        textUser.text = "username:"+username
        textEmail.text = "email:"+email

    }
}