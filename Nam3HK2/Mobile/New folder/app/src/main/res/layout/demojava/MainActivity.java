package layout.demojava;

import androidx.appcompat.app.AppCompatActivity;
import android.view.Window;
import android.view.WindowManager;


import android.os.Bundle;

import com.example.demojava.R;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        requestWindowFeature(Window.FEATURE_NO_TITLE);
        this.getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);

        setContentView(R.layout.activity_main);

        btnDangnhap =(Button) findViewById(R.id.btnDangNhap);
        editTextname = (EditText) findViewById(R.id.editTextName);
        editTextpass = (EditText) findViewById(R.id.editTextPassword);

        btnDangnhap.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
//viết code
                if(editTextname.getText().toString().equals("admin")
                        && editTextpass.getText().toString().equals("admin")){
                    txtNoiDung1.setText("Đăng nhập thành công!");
                }else{
                    txtNoiDung1.setText("Đăng nhập thất bại" +
                            editTextpass.getText().toString());
                }
            }
        });
    }
}