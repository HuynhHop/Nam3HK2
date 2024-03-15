package com.example.demojava2;

import android.content.Intent;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.view.WindowInsetsController;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

import org.w3c.dom.Text;

public class MainActivity extends AppCompatActivity {

    Button btnDangNhap;

    Button btnChuyenTrang;
    EditText editTextname, editTextpass;
    TextView txtNoiDung1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        requestWindowFeature(Window.FEATURE_NO_TITLE);
        this.getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);

        setContentView(R.layout.activity_main);

        btnDangNhap = (Button) findViewById(R.id.btnDangNhap);
        btnChuyenTrang = (Button) findViewById(R.id.btnChuyenTrang);
        editTextname = (EditText) findViewById(R.id.editTextName);
        editTextpass = (EditText) findViewById(R.id.editTextPassword);
        txtNoiDung1 = findViewById(R.id.txtNoiDung1);

        btnDangNhap.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (editTextname.getText().toString().equals("admin")
                        && editTextpass.getText().toString().equals("admin")) {
                    txtNoiDung1.setText("Đăng nhập thành công!");
                } else {
                    txtNoiDung1.setText("Đăng nhập thất bại    " +  editTextpass.getText().toString());
                }
            }
        });

        btnChuyenTrang.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity.this, MainActivity2.class);
                startActivity(intent);
            }
        });
    }
}