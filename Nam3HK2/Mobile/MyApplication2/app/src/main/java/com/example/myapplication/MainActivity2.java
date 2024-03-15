package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;

import java.util.ArrayList;

public class MainActivity2 extends AppCompatActivity {

    ListView listView;
    EditText editText1;
    Button btnNhap;
    Button btnCapNhat;
    ArrayList<MonHoc> arrayList;
    MonHocAdapter adapter;
    private void AnhXa() {
//            gridView = (GridView) findViewById(R.id.gridview1);
        editText1 = (EditText) findViewById(R.id.editText1);
        btnNhap = (Button) findViewById(R.id.btnNhap);
        btnCapNhat = (Button) findViewById(R.id.btnCapNhat);
//Thêm dữ liệu vào List
        arrayList = new ArrayList<>();
        arrayList.add(new MonHoc("Java","Java 1",R.drawable.java1));
        arrayList.add(new MonHoc("C#","C# 1",R.drawable.c));
        arrayList.add(new MonHoc("PHP","PHP 1",R.drawable.php));
        arrayList.add(new MonHoc("Kotlin","Kotlin 1",R.drawable.kotlin));
        arrayList.add(new MonHoc("Dart","Dart 1",R.drawable.dart));
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        AnhXa();
//Tạo Adapter
        adapter = new MonHocAdapter(MainActivity2.this,
                R.layout.row_monhoc, arrayList
        );
        listView.setAdapter(adapter);
    }
}