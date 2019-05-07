# -*- coding:utf-8 -*-
import random
lbtIntoInfoBasic = [{"familyIsKnown": "",
						 "loanPurpose": "2",
						 "monthPayment": "5000",
						 "applyPeriod": "24",
						 "loanPurposeDetail": "",
						 "prodRepaymentWay": "AC10001",
						 "prodServiceRate": "1",
						 "isEms": "",
						 "appProductType": "PTL150400003",
						 "maxAppAmount": "30000",
						 "customerChannel": "4",
						 "remark": "备注"
						 }]
lbtCustomerBasic = [{"nation": "汉族",
						 "cardStartT": "",
						 "cardEndT": "",
						 "hometownAreacode": "110101",
						 "hometownAddr": "朝阳区淮海路",
						 "Hdegree": "1",
						 "marrStatus": "2",
						 "hasChild": "1",
						 "childCount": "",
						 "inCityYear": "2010",
						 "mobilePhone": "13691188821",
						 "hasTelephone": "1",
						 "telephoneAreaCode": "",
						 "telphone": "",
						 "email": "111@163.COM",
						 "currentAreacode": "110101",
						 "currentAddr": "朝阳街道",
						 "homeType": "2",
						 "hMonPayment": "",
						 "homePartner": "",
						 "afterTaxMonthlyIncome": "20000",
						 "famMonPay": "",
						 "maxCreditAmount": "",
						 "customerSource": "1",
						 "birthday": "1980-10-21",
						 "sex": ""
						 }]
lbtCustomerJob = [{"jName": "捷越联合",
					   "jAddrAreacode": "110101",
					   "jAddr": "太平小区",
					   "jDept": "",
					   "jPosition": "1",
					   "jType": "1",
					   "jMonIncome": "",
					   "jPayType": "1",
					   "jPhoneAreaCode": "010",
					   "jPhone": "2715896",
					   "jEnterT": "1997",
					   "jMonPayT": ""
					   }]
lbTIntoInfoHouse = [{"houseType":"1",
						"houseBuildArea":"120",
						"housePrice":"30000",
						"houseAddrAreacode":"110102",
						"houseDetailAddr":"昌平区",
						"houseAddr":"河南省郑州市昌平区替阿宁加油2号",
						"housePurchasedYears":"15",
						"houseLoYearLimit":"20",
						"houseProRightRate":"10",
						"houseMonthlyPayment":"5000",
						"houseLoBalance":"230000",
						"houseAddrPostcode":"266000",
						}]
LbtIntoInfoInsurPolicy = [{"contractEffectDate":"2010-01-01",
						"firstPaymentDate":"2010-01-10",
						"insurancePeriod":"15",
						"payPeriod":"10",
						"insurancePremium":"50000",
						"insuranceAmount":"500000",
						"paymentMethod":"2"
						}]
LbTIntoInfoManage = [{"comType": "3",
						  "shareholdRatio": "50",
						  "comAddr": "1",
						  "registerDate": "1999-01-01",
						  "comEmpCount": "1"
						  }]
lbtIntoInfoContact = [{"contactType": "3",
						   "conRelation": "2",
						   "conName": "小明",
						   "conPhone": "15800260036",
						   "conCompany": "",
						   "conHomeAreacode": "",
						   "conHomeDetailAddr": "",
						   "conHomeAddr": "",
						   "conJobAreacode": "",
						   "conJobDetailAddr": "",
						   "conJobAddr": "",
						   },
						  {"contactType": "2",
						   "conRelation": "4",
						   "conName": "小明",
						   "conPhone": "15800260036",
						   "conCompany": "",
						   "conHomeAreacode": "",
						   "conHomeDetailAddr": "",
						   "conHomeAddr": "",
						   "conJobAreacode": "",
						   "conJobDetailAddr": "",
						   "conJobAddr": "",
						   }]
lbtIntoInfoBankCard = [{"accountName": "营销进件",
							"bankCardAccount": "23423424",
							"bankCode": "105",
							"bankProvAreacode": "110100",
							"bankCityAreacode": "110100",
							"subBranchName": "朝阳支行",
							"bankReservedPhone": "13691188821",
							"isLoanType": "1",
							"isReceiveType": "1"
							}]
lbtSerialInfoLiability = [{"accEndNo": "6678",
						"accType": "1",
						"accMonSer1": "500",
						"accMonSer2": "2000",
						"accMonSer3": "800",
						"accMonSer4": "1000",
						"accMonSer5": "7000",
						"accMonSer6": "1000",
						"accMonSer7": "1000",
						"avgMonthIncome": "10000",
						"cheMonIncome": "1200",
						"startFromMonthSelect": "4",
						}]
lbtLiability = [{"creditReportState": "1",
					 "creditVersionType": "1",
					 "accQCount": "1",
					 "accCAuditCount": "1",
					 "loanAuditCount": "1",
					 "currOverdueAmount": "5000",
					 "credit24Overdue": "",
					 "credit24OverdueCount": "",
					 "credit24ContinueOverdue": "",
					 "year5CreaditOverdueCount": "1",
					 "cardSumDebt": "",
					 "loan24Overdue": "",
					 "loan24OverdueCount": "",
					 "loan24ContinueOverdue": "",
					 "year5LoanOverdueCount": "1",
					 "debtSum": "",
					 "incomeDebtRatio": "",
					 "enableCreditCrad": "",
					 "openedCount": "",
					 "isLoanInfo": ""
					 }]
lbtSerialInfo = [{"cheMonIncome": "2500",
					  "rescindRatio": "100",
					  "cashRatio": "100",
					  "industryProfitRate": "70",
					  "sharesRatio": "80",
					  "insteadMonthIncome": "1000",
					  "remark": "流水信息"}]
list = [lbtIntoInfoBasic, lbtCustomerBasic, lbtCustomerJob, lbTIntoInfoHouse, LbtIntoInfoInsurPolicy, LbTIntoInfoManage,
		lbtIntoInfoContact, lbtIntoInfoBankCard, lbtSerialInfoLiability, lbtLiability, lbtSerialInfo]

list1=('lbtIntoInfoBasic', 'lbtCustomerBasic', 'lbtCustomerJob', 'lbtIntoInfoHouse', 'lbtIntoInfoInsurPolicy', 'lbtIntoInfoManage',
			'lbtIntoInfoContact', 'lbtIntoInfoBankCard', 'lbtSerialInfoLiability', 'lbtLiability', 'lbtSerialInfo')

list2=('lbtIntoInfoBasic', 'lbtCustomerBasic', 'lbtCustomerJob', 'lbTIntoInfoHouse', 'LbTIntoInfoInsurPolicy', 'LbtIntoInfoManage',
			'lbtIntoInfoContact', 'lbtIntoInfoBankCard', 'lbtSerialInfoLiability', 'lbtLiability', 'lbtSerialInfo')
