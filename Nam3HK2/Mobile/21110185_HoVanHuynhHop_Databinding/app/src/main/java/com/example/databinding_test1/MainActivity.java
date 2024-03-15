package com.example.databinding_test1;

import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.DataBindingUtil;

import android.os.Bundle;

import com.example.databinding_test1.databinding.ActivityMainBinding;

public class MainActivity extends AppCompatActivity {
    private UserModel userModel;
    private ActivityMainBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding= DataBindingUtil.setContentView(this,R.layout.activity_main);
        userModel=new UserModel ("Ho","Hop");
        binding.setUser(userModel);
        userModel.setFirstName("Vinh");
        userModel.setLastName("Tran");
    }
}