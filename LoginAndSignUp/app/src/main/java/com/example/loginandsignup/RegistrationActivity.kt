package com.example.loginandsignup

import android.annotation.SuppressLint
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Toast

class RegistrationActivity : AppCompatActivity() {

    lateinit var doRegistration: Button
    lateinit var editName: EditText
    lateinit var editUName: EditText
    lateinit var editUEmail: EditText
    lateinit var editUPassword: EditText

    @SuppressLint("MissingInflatedId")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_registration)

        doRegistration = findViewById(R.id.registrationBtn)
        editName = findViewById(R.id.editname)
        editUName = findViewById(R.id.editUserName)
        editUEmail = findViewById(R.id.editemail)
        editName = findViewById(R.id.editname)
        editUPassword = findViewById(R.id.editpassword)

        doRegistration.setOnClickListener{
            if(editName.text.toString().isNotEmpty() &&
                editUName.text.toString().isNotEmpty() &&
                editUEmail.text.toString().isNotEmpty() &&
                editUPassword.text.toString().isNotEmpty() ){
                Toast.makeText(this,"Registration Successful!", Toast.LENGTH_SHORT).show()
                startActivity(Intent(this,MainActivity::class.java))
            }else{
                Toast.makeText(this,"Registration failed!", Toast.LENGTH_SHORT).show()
            }
        }

    }
}