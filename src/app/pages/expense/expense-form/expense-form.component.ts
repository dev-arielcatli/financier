import { Component, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { Expense, SafeDisplayExpense } from '../expense.model';
import {
  MAT_DIALOG_DATA,
  MatDialogActions,
  MatDialogContent,
  MatDialogRef,
} from '@angular/material/dialog';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'fn-expense-form',
  imports: [
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatDialogActions,
    MatButtonModule,
  ],
  templateUrl: './expense-form.component.html',
  styleUrl: './expense-form.component.scss',
})
export class ExpenseFormComponent {
  private formBuilder = inject(FormBuilder);

  expenseDialogRef = inject(MatDialogRef<ExpenseFormComponent>);

  dialogData: SafeDisplayExpense = inject(MAT_DIALOG_DATA);

  expenseForm = this.formBuilder.group({
    id: [''],
    name: ['', Validators.required],
    description: [''],
    quantity: [1],
    amount: [0],
    date: [''],
    createdAt: [''],
    updatedAt: [''],
    address: [''],
    tags: [['']],
  });

  constructor() {
    if (this.dialogData) {
      this.expenseForm.patchValue(this.dialogData);
    }
  }

  onSave(): void {
    if (this.expenseForm.valid) {
      this.expenseDialogRef.close(this.expenseForm.value);
    }
  }

  onCancel(): void {
    this.expenseDialogRef.close();
  }
}
