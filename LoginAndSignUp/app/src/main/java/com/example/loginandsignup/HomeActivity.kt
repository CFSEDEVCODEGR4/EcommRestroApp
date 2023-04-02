package com.example.loginandsignup

import android.annotation.SuppressLint
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.ArrayAdapter
import android.widget.ListView
import android.widget.SearchView
import android.widget.Toast
import androidx.appcompat.widget.Toolbar

class HomeActivity : AppCompatActivity() {

    lateinit var searchView: SearchView
    lateinit var menuItemList: ListView

    private lateinit var myMenuToolbar: Toolbar

    @SuppressLint("MissingInflatedId")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_home)
       //supportActionBar!!.setDisplayHomeAsUpEnabled(true)

        myMenuToolbar = findViewById(R.id.myMenuToolbar)
        myMenuToolbar.title = "Menu"
        setSupportActionBar(myMenuToolbar)

        searchView = findViewById(R.id.searchView)
        menuItemList = findViewById(R.id.menuItemList)

        val menuItem = arrayOf("veg Thali","punjabi thali","paratha","pizza")

        val menuItemAdapter: ArrayAdapter<String> = ArrayAdapter(

            this,android.R.layout.simple_list_item_1,
            menuItem
        )

        menuItemList.adapter = menuItemAdapter;

        searchView.setOnQueryTextListener(object : SearchView.OnQueryTextListener{
            override fun onQueryTextSubmit(p0: String?): Boolean {
               searchView.clearFocus()
                if(menuItem.contains(p0)){

                    menuItemAdapter.filter.filter(p0)

                }
                return false
            }

            override fun onQueryTextChange(p0: String?): Boolean {
                menuItemAdapter.filter.filter(p0)
                return false
            }

        })

        myMenuToolbar.setNavigationOnClickListener{
            //Toast.makeText(this,"Navigation Menu clicked", Toast.LENGTH_SHORT).show()
            startActivity(Intent(this,MainActivity::class.java))
        }
    }
}