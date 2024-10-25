CREATE TABLE Address (
  ID          number(5) NOT NULL, 
  Street      varchar2(255) NOT NULL, 
  PostCode    varchar2(15) NOT NULL, 
  Town        varchar2(255) NOT NULL, 
  CountryCode varchar2(2) NOT NULL, 
  PRIMARY KEY (ID));
CREATE TABLE BoM (
  ProductCode   varchar2(10) NOT NULL, 
  ComponentCode varchar2(10) NOT NULL, 
  Quantity      number(10) NOT NULL, 
  PRIMARY KEY (ProductCode, 
  ComponentCode));
CREATE TABLE BoO (
  Step              number(3) NOT NULL, 
  ProductFamilyCode varchar2(10) NOT NULL, 
  OperationID       number(4) NOT NULL, 
  PRIMARY KEY (Step, 
  ProductFamilyCode, 
  OperationID));
CREATE TABLE Component (
  Code        varchar2(10) NOT NULL, 
  Description varchar2(255) NOT NULL, 
  PRIMARY KEY (Code));
CREATE TABLE Costumer (
  ID           number(5) NOT NULL, 
  Name         varchar2(255) NOT NULL, 
  Contact      number(10) NOT NULL, 
  AddressID    number(5) NOT NULL, 
  CostumerType varchar2(255), 
  PRIMARY KEY (ID));
CREATE TABLE CostumerOrder (
  ID           number(5) NOT NULL, 
  DeliveryDate date NOT NULL, 
  OrderDate    date NOT NULL, 
  CostumerID   number(5) NOT NULL, 
  PRIMARY KEY (ID));
CREATE TABLE CostumerType (
  Type varchar2(255) NOT NULL, 
  PRIMARY KEY (Type));
CREATE TABLE Country (
  Code varchar2(2) NOT NULL, 
  Name varchar2(255) NOT NULL, 
  PRIMARY KEY (Code));
CREATE TABLE Operation (
  ID   number(4) NOT NULL, 
  Name varchar2(255) NOT NULL, 
  PRIMARY KEY (ID));
CREATE TABLE Product (
  Code              varchar2(10) NOT NULL, 
  Name              varchar2(50) NOT NULL, 
  Description       varchar2(255) NOT NULL, 
  ProductFamilyCode varchar2(10) NOT NULL, 
  PRIMARY KEY (Code));
CREATE TABLE ProductFamily (
  Code varchar2(10) NOT NULL, 
  Name varchar2(255) NOT NULL, 
  PRIMARY KEY (Code));
CREATE TABLE ProductOrder (
  OrderID     number(5) NOT NULL, 
  ProductCode varchar2(10) NOT NULL, 
  Quantity    number(3) NOT NULL, 
  PRIMARY KEY (OrderID, 
  ProductCode));
CREATE TABLE Vatin (
  Vat         number(9) NOT NULL, 
  CountryCode varchar2(2) NOT NULL, 
  CostumerID  number(5) NOT NULL, 
  PRIMARY KEY (Vat, 
  CountryCode));
CREATE TABLE Workstation (
  ID                  number(5) NOT NULL, 
  Name                varchar2(255) NOT NULL, 
  Description         varchar2(255) NOT NULL, 
  WorkstationTypeCode varchar2(5) NOT NULL, 
  PRIMARY KEY (ID));
CREATE TABLE WorkstationType (
  Code varchar2(5) NOT NULL, 
  Name varchar2(255) NOT NULL, 
  PRIMARY KEY (Code));
CREATE TABLE WorkstationTypeOperation (
  WorkstationTypeCode varchar2(5) NOT NULL, 
  OperationID         number(4) NOT NULL, 
  PRIMARY KEY (WorkstationTypeCode, 
  OperationID));
ALTER TABLE BoO ADD CONSTRAINT FKBoO815244 FOREIGN KEY (ProductFamilyCode) REFERENCES ProductFamily (Code);
ALTER TABLE CostumerOrder ADD CONSTRAINT FKCostumerOr8543 FOREIGN KEY (CostumerID) REFERENCES Costumer (ID);
ALTER TABLE Costumer ADD CONSTRAINT FKCostumer550618 FOREIGN KEY (AddressID) REFERENCES Address (ID);
ALTER TABLE BoM ADD CONSTRAINT FKBoM90229 FOREIGN KEY (ProductCode) REFERENCES Product (Code);
ALTER TABLE BoM ADD CONSTRAINT FKBoM840203 FOREIGN KEY (ComponentCode) REFERENCES Component (Code);
ALTER TABLE WorkstationTypeOperation ADD CONSTRAINT FKWorkstatio924771 FOREIGN KEY (WorkstationTypeCode) REFERENCES WorkstationType (Code);
ALTER TABLE WorkstationTypeOperation ADD CONSTRAINT FKWorkstatio670867 FOREIGN KEY (OperationID) REFERENCES Operation (ID);
ALTER TABLE BoO ADD CONSTRAINT FKBoO346839 FOREIGN KEY (OperationID) REFERENCES Operation (ID);
ALTER TABLE Vatin ADD CONSTRAINT FKVatin149569 FOREIGN KEY (CountryCode) REFERENCES Country (Code);
ALTER TABLE Vatin ADD CONSTRAINT FKVatin748732 FOREIGN KEY (CostumerID) REFERENCES Costumer (ID);
ALTER TABLE Address ADD CONSTRAINT FKAddress615272 FOREIGN KEY (CountryCode) REFERENCES Country (Code);
ALTER TABLE Costumer ADD CONSTRAINT FKCostumer393272 FOREIGN KEY (CostumerType) REFERENCES CostumerType (Type);
ALTER TABLE ProductOrder ADD CONSTRAINT FKProductOrd905990 FOREIGN KEY (ProductCode) REFERENCES Product (Code);
ALTER TABLE ProductOrder ADD CONSTRAINT FKProductOrd755606 FOREIGN KEY (OrderID) REFERENCES CostumerOrder (ID);
ALTER TABLE Workstation ADD CONSTRAINT FKWorkstatio143370 FOREIGN KEY (WorkstationTypeCode) REFERENCES WorkstationType (Code);
ALTER TABLE Product ADD CONSTRAINT FKProduct42722 FOREIGN KEY (ProductFamilyCode) REFERENCES ProductFamily (Code);
