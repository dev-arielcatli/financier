import { Component, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule } from '@angular/forms';
import { Expense } from './expense.model';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import {
  MatDialog,
  MatDialogModule,
  MatDialogRef,
} from '@angular/material/dialog';
import { ExpenseFormComponent } from './expense-form/expense-form.component';

@Component({
  selector: 'fn-expense',
  imports: [
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatDialogModule,
  ],
  templateUrl: './expense.component.html',
  styleUrl: './expense.component.scss',
})
export class ExpenseComponent {
  expenseDialog = inject(MatDialog);

  onAddExpense(): void {
    console.log('Add Expense');
    this.expenseDialog.open(ExpenseFormComponent, {});
  }
}
