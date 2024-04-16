def calculate_nrtci(pci, cellid, gnbid, gnbid_length):
    # 將 gnbid 轉換為二進制字符串
    gnbid_bin = format(gnbid, f'0{gnbid_length}b')
    cellid_bin = format(cellid, f'0{36-gnbid_length}b')
    pci_bin = format(pci, '010b')

    # 組合 nrtci
    if gnbid_length == 22:
        nrtci_bin = gnbid_bin + cellid_bin + pci_bin + '0' * 18
    elif gnbid_length == 32:
        nrtci_bin = gnbid_bin + cellid_bin + pci_bin + '0' * 18
    else:
        raise ValueError("Invalid gnbid_length. Supported values are 22 or 32.")

    # 將二進制字符串轉換為整數
    nrtci = int(nrtci_bin, 2)
    return nrtci

def calculate_nci(cellid, gnbid, gnbid_length):
    # 將 gnbid 轉換為二進制字符串
    gnbid_bin = format(gnbid, f'0{gnbid_length}b')
    cellid_bin = format(cellid, f'0{36-gnbid_length}b')

    # 組合 nci
    if gnbid_length == 22:
        nci_bin = gnbid_bin + cellid_bin
    elif gnbid_length == 32:
        nci_bin = gnbid_bin + cellid_bin
    else:
        raise ValueError("Invalid gnbid_length. Supported values are 22 or 32.")

    # 將二進制字符串轉換為十六進制
    nci = f'{int(nci_bin, 2):09X}'
    #nci = hex(nci_bin)
    return nci

def main():
    # 接收輸入
    gnbid = int(input("請輸入 gnbid："))
    gnbid_length = int(input("請輸入 gnbid_length (22/32):"))
    cellid = int(input("請輸入 cellid："))
    pci = int(input("請輸入 pci："))

    # 計算 nrtci
    result = calculate_nrtci(pci, cellid, gnbid, gnbid_length)
    res_nci = calculate_nci(cellid, gnbid, gnbid_length)
    print(f"計算結果：nrtci(dec) = {result}, nci(hex) = {res_nci}")

if __name__ == "__main__":
    main()

# 測試函式 , ctrl+K 進行註解，ctrl+/ 取消註解
# pci_input = 11  # 替換為您的實際值
# cellid_input = 1  # 替換為您的實際值
# gnbid_input = 135  # 替換為您的實際值
# gnbid_length_input = 32  # 替換為您的實際值

# result = calculate_nrtci(pci_input, cellid_input, gnbid_input, gnbid_length_input)
# res_nci = calculate_nci(cellid_input, gnbid_input, gnbid_length_input)
# print(f"計算結果：nrtci = {result}, nci = {res_nci}")
