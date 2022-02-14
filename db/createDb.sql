create database if not exists Projekt_06;
use Projekt_06;

create table if not exists Lied_Künstler 
( 
	Id int auto_increment unique key primary key,
    kÜnstlerId int (40),
    LiedId int (40)
    );
create table if not exists Lied (
	LiedId int auto_increment unique key primary key,
	Künsterzahl int (40),
	KünsterlId int (40),
	Liedname varchar (40),
	Erscheinungsdatum date 
);

create table if not exists Manager (
	ManagerId int auto_increment unique key primary key,
	Vorname varchar (40),
	Nachname varchar (40),
	Firma varchar (40),
	Künstler_anzahl int (40) 
);

create table if not exists Lied_Künstler 
( 
	Id int auto_increment unique key primary key,
    KünstlerId int (40),
    LiedId int (40),
    constraint KünstlerForeignKey foreign key (KünstlerId) references Künstler (KünstlerId),
    constraint LiedForeignKey foreign key (LiedId) references Lied (LiedId)
    );
    
create table if not exists Künstler (
	KünstlerId int auto_increment unique key primary key,
	Gehalt int (40),
	Herkunftsland varchar (40),
	Vorname varchar (40),
	Nachname varchar (40),
    ManagerId int (40),
    constraint mangerForeignKey foreign key (ManagerId) references Manager (ManagerId)
);