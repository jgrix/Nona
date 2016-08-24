package com.grixie.Nona;
import java.net.InetAddress;
import java.net.Socket;
import java.io.*;
import java.net.UnknownHostException;

/**
 * Created by jgrix2 on 8/5/16.
 */


public class TCPClient{

    private String serverMessage;
    public static String ServerIP = "19.58.196.48";
    public static int ServerPort = 5566;

    private OnMessageReceived mMessageListener = null;

    private boolean mRun = false;

    PrintWriter out;
    BufferedReader in;


    public TCPClient(OnMessageReceived listener) {
        mMessageListener = listener;
    }


    public void sendMessage(String message){
        if (out != null && !out.checkError()) {
            out.println(message);
            out.flush();
        }
    }

    public interface OnMessageReceived {
         void messageReceived(String message);
    }

    public void stopClient(){
        mRun = false;
    }

    public void run() {

        mRun = true;

        Socket socket = null;
        try {
            InetAddress serverAddr = InetAddress.getByName(ServerIP);
            socket = new Socket(serverAddr, ServerPort);
        } catch (UnknownHostException e) {
            e.printStackTrace();
            return;
        } catch (IOException e) {
            e.printStackTrace();
            return;
        }

        try {
            out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(socket.getOutputStream())), true);
        }
        catch (Exception e) {
            e.printStackTrace();
            return;
        }

        try {
            in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        }
        catch (Exception e){
            e.printStackTrace();
        }

        try {
            while (mRun) {

                serverMessage = in.readLine();


                if (serverMessage != null && mMessageListener != null) {
                    mMessageListener.messageReceived(serverMessage);
                }
                serverMessage = null;

                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }


            }

            socket.close();
        }catch (IOException e) {
            e.printStackTrace();
        }




    }


}
