package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    ListView listView;
    ArrayList<String> arrayList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //ánh xạ
        listView = (ListView) findViewById(R.id.listview1);
        arrayList = new ArrayList<>();
        arrayList.add("Java");
        arrayList.add("C#");
        arrayList.add("PHP");
        arrayList.add("Kotlin");
        arrayList.add("Dart");

        //Tạo ArrayAdapter
        ArrayAdapter adapter = new ArrayAdapter(
                MainActivity.this,
                android.R.layout.simple_list_item_1,
                arrayList
        );

        //truyền dữ liệu từ adapter ra listview
        listView.setAdapter(adapter);

        // Bắt sự kiện click trên từng dòng của ListView
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                // Xử lý sự kiện khi một dòng được click
                String selectedItem = (String) parent.getItemAtPosition(position);
                Toast.makeText(MainActivity.this, "Đã chọn: " + selectedItem, Toast.LENGTH_SHORT).show();
            }
        });

        // Bắt sự kiện giữ (long click) trên từng dòng của ListView
        listView.setOnItemLongClickListener(new AdapterView.OnItemLongClickListener() {
            @Override
            public boolean onItemLongClick(AdapterView<?> parent, View view, int position, long id) {
                // Xử lý sự kiện khi một dòng được giữ (long click)
                String selectedItem = (String) parent.getItemAtPosition(position);
                Toast.makeText(MainActivity.this, "Bạn đang giữ: " + selectedItem, Toast.LENGTH_SHORT).show();

                // Trả về true để ngăn chặn sự kiện click thông thường sau sự kiện giữ
                return true;
            }
        });

        EditText editText1;
        Button btnNhap;

        editText1 = (EditText) findViewById(R.id.editText1);
        btnNhap = (Button) findViewById(R.id.btnNhap);

        btnNhap.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String name = editText1.getText().toString();
                arrayList.add(name);
                adapter.notifyDataSetChanged();
            }
        });

        //Khai báo
        Button btnCapnhat;
        final int[] vitri = {-1};

//ánh xạ
        btnCapnhat = (Button) findViewById(R.id.btnCapnhat);

//bắt sự kiện trên từng dòng của Listview
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                editText1.setText(arrayList.get(i));
                vitri[0] = i;
            }
        });

        btnCapnhat.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (vitri[0] != -1) {
                    // Kiểm tra xem vitri[0] có giá trị hợp lệ không
                    arrayList.set(vitri[0], editText1.getText().toString());
                    adapter.notifyDataSetChanged();
                } else {
                    // Xử lý trường hợp không có dòng nào được chọn trước đó
                    Toast.makeText(MainActivity.this, "Vui lòng chọn một dòng trước khi cập nhật", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}