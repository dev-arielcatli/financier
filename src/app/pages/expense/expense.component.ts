import { AfterViewInit, Component, inject, ViewChild } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatTableDataSource, MatTableModule } from '@angular/material/table';

import { MatInputModule } from '@angular/material/input';
import { MatDialog, MatDialogModule } from '@angular/material/dialog';
import { ExpenseFormComponent } from './expense-form/expense-form.component';
import { Expense } from './expense.model';
import { mockExpenses } from './mocks/expenses.mock';
import { CommonModule } from '@angular/common';

import { MatPaginator, MatPaginatorModule } from '@angular/material/paginator';

@Component({
  selector: 'fn-expense',
  imports: [
    CommonModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatDialogModule,
    MatTableModule,
    MatPaginatorModule,
  ],
  templateUrl: './expense.component.html',
  styleUrl: './expense.component.scss',
})
export class ExpenseComponent implements AfterViewInit {
  @ViewChild(MatPaginator) expenseTablePaginator!: MatPaginator;

  expenseDialog = inject(MatDialog);
  expenseColumns: string[] = [
    'name',
    'description',
    'quantity',
    'amount',
    'date',
  ];
  expenseDataSource = new MatTableDataSource<Expense>(mockExpenses);

  ngAfterViewInit(): void {
    this.expenseDataSource.paginator = this.expenseTablePaginator;
  }

  onAddExpense(): void {
    console.log('Add Expense');
    this.expenseDialog.open(ExpenseFormComponent, {});
  }
}
