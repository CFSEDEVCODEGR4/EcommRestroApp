package com.example.loginandsignup

import android.annotation.SuppressLint
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import androidx.appcompat.widget.Toolbar

class MainActivity : AppCompatActivity() {

    lateinit var  myToolbar: Toolbar
    lateinit var doLogin: Button
    lateinit var doregistration: Button

    lateinit var editUName: EditText
    lateinit var editUPassword: EditText


    @SuppressLint("MissingInflatedId")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        myToolbar = findViewById(R.id.myToolbar)
        myToolbar.title = "Restro"
        setSupportActionBar(myToolbar)

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

        myToolbar.setNavigationOnClickListener{
            Toast.makeText(this,"Navigation Menu clicked",Toast.LENGTH_SHORT).show()
        }

        doregistration.setOnClickListener{
            startActivity(Intent(this,RegistrationActivity::class.java))
        }

    }

    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.mainmenu, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        var iemview = item.itemId

        when(iemview){
            R.id.add->Toast.makeText(applicationContext,"Addclicked",Toast.LENGTH_SHORT).show()
            R.id.notify->Toast.makeText(applicationContext," Notification clicked",Toast.LENGTH_SHORT).show()
        }
        return false
    }

}