using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Diagnostics;
using System.Threading;


namespace classic_cipher
{
    public partial class Form1 : Form
    {


        void TextWrite(string name, string data)
        {
            string path = @"input files\\" + name + ".txt";
            if (File.Exists(path))
            {
                File.Delete(path);
            }
            StreamWriter text = new StreamWriter(path);
            text.Write("{0}\r\n", data);
            text.Close();
        }
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {
            
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (checkBox1.Checked)
            {
                TextWrite("Caesar\\caesar_plain", textBox1.Text);
                TextWrite("All Keys\\Caesar_key", textBox2.Text);
            }
            else if (checkBox2.Checked)
            {
                TextWrite("Hill\\hill_plain", textBox1.Text);
                TextWrite("All Keys\\Hill_key", textBox2.Text);
            }
            else if (checkBox3.Checked)
            {
                TextWrite("PlayFair\\playfair_plain", textBox1.Text);
                TextWrite("All Keys\\PlayFair_key", textBox2.Text);
            }
            else if (checkBox4.Checked)
            {
                TextWrite("Vernam\\vernam_plain", textBox1.Text);
                TextWrite("All Keys\\Vernam_key", textBox2.Text);
            }
            else if (checkBox5.Checked)
            {
                TextWrite("Vigenere\\vigenere_plain", textBox1.Text);
                TextWrite("All Keys\\Vigenere_key", textBox2.Text);
            }
            else if (checkBox6.Checked)
            {
                TextWrite("Vigenere\\vigenere_plain", textBox1.Text);
                TextWrite("All Keys\\Vigenere_key", textBox2.Text);
            }


            //call python

            Process.Start("Main.exe");
            Thread.Sleep(500);
            //show cipher
            string path = Directory.GetCurrentDirectory();
            path+= "\\ouput files\\";
            
            string[] readnames = File.ReadAllLines(path+"caesar_cipher.txt");
            if (checkBox1.Checked)
            {
                
               
                //Path.Combine(Directory.GetCurrentDirectory(), "\\ouput files");
                readnames = File.ReadAllLines(path+"caesar_cipher.txt");
            }
            else if (checkBox2.Checked)
            {
                
                //Path.Combine(Directory.GetCurrentDirectory(), "\\ouput files");
                readnames = File.ReadAllLines(path+"Hill_cipher.txt");
            }
            else if (checkBox3.Checked)
            {
               
                // Path.Combine(Directory.GetCurrentDirectory(), "\\ouput files");
                readnames = File.ReadAllLines(path+"play fair cipher.txt");
            }
            else if (checkBox4.Checked)
            {
                
                // Path.Combine(Directory.GetCurrentDirectory(), "\\ouput files");
                readnames = File.ReadAllLines(path+"Vernam_cipher.txt");
            }
            else if (checkBox5.Checked)
            {
                
                // Path.Combine(Directory.GetCurrentDirectory(), "\\ouput files");
                readnames = File.ReadAllLines(path + "Vigenere_cipher auto mode.txt");
            }
            else if (checkBox6.Checked)
            {
               
                //Path.Combine(Directory.GetCurrentDirectory(), "\\ouput files");
                readnames = File.ReadAllLines(path+"Vigenere_cipher repeating mode.txt");
            }
            textBox3.Text = "";
            for (int i = 0; i < readnames.Length; i++)
            {

                textBox3.Text += readnames[i];
            }
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            checkBox2.Checked = false;
            checkBox3.Checked = false;
            checkBox4.Checked = false;
            checkBox5.Checked = false;
            checkBox6.Checked = false;
        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {
            checkBox1.Checked = false;

            checkBox3.Checked = false;
            checkBox4.Checked = false;
            checkBox5.Checked = false;
            checkBox6.Checked = false;
        }

        private void checkBox3_CheckedChanged(object sender, EventArgs e)
        {
            checkBox1.Checked = false;
            checkBox2.Checked = false;

            checkBox4.Checked = false;
            checkBox5.Checked = false;
            checkBox6.Checked = false;
        }

        private void checkBox4_CheckedChanged(object sender, EventArgs e)
        {
            checkBox1.Checked = false;
            checkBox2.Checked = false;
            checkBox3.Checked = false;

            checkBox5.Checked = false;
            checkBox6.Checked = false;
        }

        private void checkBox5_CheckedChanged(object sender, EventArgs e)
        {
            checkBox1.Checked = false;
            checkBox2.Checked = false;
            checkBox3.Checked = false;
            checkBox4.Checked = false;

            checkBox6.Checked = false;
        }

        private void checkBox6_CheckedChanged(object sender, EventArgs e)
        {

            checkBox1.Checked = false;
            checkBox2.Checked = false;
            checkBox3.Checked = false;
            checkBox4.Checked = false;
            checkBox5.Checked = false;
        }
    }
}
