package com.example.LoginApp

import android.annotation.SuppressLint
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText

class Registration : AppCompatActivity() {

    private lateinit var doRegistration: Button
    lateinit var editName: EditText
    lateinit var editUserName: EditText
    lateinit var editPassword: EditText
    lateinit var editEmail: EditText
    @SuppressLint("MissingInflatedId")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_registration)

        doRegistration = findViewById(R.id.signupBtn)
        editName = findViewById(R.id.editname)
        editUserName = findViewById(R.id.editUserName)
        editEmail = findViewById(R.id.editemail)
        editPassword= findViewById(R.id.editpassword)

        doRegistration.setOnClickListener{
            startActivity(Intent(this,HomeActivity::class.java)
                .putExtra("Name",editName.text.toString())
                .putExtra("Name",editUserName.text.toString())
                .putExtra("Name",editEmail.text.toString())
                .putExtra("Name",editPassword.text.toString())

            )
        }

    }
}