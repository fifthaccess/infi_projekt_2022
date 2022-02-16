create database if not exists Projekt_06;
use Projekt_06;

create table if not exists Lied_Kuenstler 
( 
	Id int auto_increment unique key primary key,
    kuenstlerId int (40),
    LiedId int (40)
    );
    
create table if not exists Lied (
	LiedId int auto_increment unique key primary key,
	Kuensterzahl int (40),
	Liedname varchar (40),
	Erscheinungsdatum date
);

create table if not exists Manager (
	ManagerId int auto_increment unique key primary key,
	Vorname varchar (40),
	Nachname varchar (40),
	Firma varchar (40),
	Kuenstler_anzahl int (40) 
);

create table if not exists Lied_Kuenstler 
( 
	Id int auto_increment unique key primary key,
    KuenstlerId int (40),
    LiedId int (40),
    constraint KuenstlerForeignKey foreign key (KuenstlerId) references Kuenstler (KuenstlerId),
    constraint LiedForeignKey foreign key (LiedId) references Lied (LiedId)
    );
    
create table if not exists Kuenstler (
	KuenstlerId int auto_increment unique key primary key,
	Gehalt int (40),0,
	
	Herkunftsland varchar (40),
	Vorname varchar (40),
	Nachname varchar (40),
    ManagerId int (40),
    constraint mangerForeignKey foreign key (ManagerId) references Manager (ManagerId)
);
