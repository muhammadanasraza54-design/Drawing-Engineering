import mysql.connector
import os

# Database Connection
db = mysql.connector.connect(
    host="mysql-15fcdecc-muhammadanasraza54-5182.g.aivencloud.com",
    port=11756,
    user="avnadmin",
    password="AVNS_aRLK6thMKERAＮG1GB5w",
    database="defaultdb"
)
cursor = db.cursor()

# OneDrive Folder Path jahan drawings hain
folder_path = r"D:\OneDrive_Data\OneDrive - The Citizens Foundation\DIGITAL LIBRARY"


# OneDrive ka base shareable link (Jo aapne copy kiya tha)
# Note: Is link ko use karke hum direct file link banayenge
base_share_link = "https://tcfpk-my.sharepoint.com/:f:/g/personal/anas_raza_tcf_org_pk/IgAmOt1Aojv9Q6jUTRG_HyoZAYpsBxMHYOdELVpnSsMhGzY?e=UcPf5s" 

print("Links update ho rahy hain...")

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_name = file
        individual_link = f"{base_share_link}&file={file_name}"
        
        # SQL Query: File name ke mutabiq link update karna
        sql = "UPDATE drawings SET file_link = %s WHERE file_name = %s"
        val = (individual_link, file_name)
        
        cursor.execute(sql, val)

db.commit()
print(f"Done! {cursor.rowcount} records update ho gaye.")
db.close()