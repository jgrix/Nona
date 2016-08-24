package com.grixie.Nona;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.text.Editable;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.grixie.Nona.R;

/**
 * Created by jgrix2 on 7/15/16.
 */
public class Frag_One extends Fragment {

    private TCPClient myclient;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        View rootview = inflater.inflate(R.layout.content_one, container, false);
        InitialSetUp(rootview);
        return rootview;
    }

    public void setClient(TCPClient x){
        myclient = x;
    }

    public void InitialSetUp(View rootView) {

        Button setTemp = (Button) rootView.findViewById(R.id.button_Set_Tempature);
        final TextView targetTempText = (TextView) rootView.findViewById(R.id.Target_Temp_Field);
        final EditText targetTemp = (EditText) rootView.findViewById(R.id.editText);

        final Button sendMessage = (Button) rootView.findViewById(R.id.Test_Message);


        setTemp.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Editable target = targetTemp.getText();
                targetTempText.setText(target);
                targetTemp.setText("");
            }
        });

        sendMessage.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(myclient != null)
                    myclient.sendMessage("Hello world!");
            }
            });



    }
}