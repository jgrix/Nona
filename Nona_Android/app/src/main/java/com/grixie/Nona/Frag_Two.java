package com.grixie.Nona;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import com.grixie.Nona.R;

/**
 * Created by jgrix2 on 7/15/16.
 */
public class Frag_Two extends Fragment {

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        View rootview =  inflater.inflate(R.layout.content_two, container, false);
        return  rootview;
    }
}
