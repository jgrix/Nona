package com.grixie.Nona;

import android.bluetooth.BluetoothDevice;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.media.AudioManager;
import android.util.Log;

/**
 * Created by jgrix2 on 7/19/16.
 */
public class SDLReceiver extends BroadcastReceiver {

    public void onReceive(Context context, Intent intent) {
        final BluetoothDevice btDevive = (BluetoothDevice) intent.getParcelableExtra(BluetoothDevice.EXTRA_DEVICE);

        if(intent.getAction().compareTo(BluetoothDevice.ACTION_ACL_CONNECTED) == 0){
            SDLService myserv = SDLService.getInstance();

            if (myserv == null) {
                Intent startIntent = new Intent(context, SDLService.class);
                startIntent.putExtras(intent);
                context.startService(startIntent);
            }
        }
        else if (intent.getAction().equals(AudioManager.ACTION_AUDIO_BECOMING_NOISY)) {
            Log.d("Audio becoming noisy!", intent.getAction());
        }

    }
}
